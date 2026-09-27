---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issue over allotment terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Terms for Change to an Issue Amount. A provision in an underwriting agreement, which allows members of the underwriting
      syndicate to purchase additional shares at the original price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Also known as a green shoe. Note that this set of terms does not refer to over-allotment as change to a the total
      issue amount issued to an individual investor. That would require separate but similar terms. FIBIM has "Over Allotment
      Amount" as an individual term.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/maximumOverAllotmentAmount
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: issue over allotment terms
type: Ontology Class
---

# issue over allotment terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms>

## Definition

Terms for Change to an Issue Amount. A provision in an underwriting agreement, which allows members of the underwriting syndicate to purchase additional shares at the original price.

## Relationships

- **Subclass of**: [OfferingDocumentTerms](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)

## Constraints

- **[maximumOverAllotmentAmount](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/maximumOverAllotmentAmount.md)**: max qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): issue over allotment terms
- **definition** (en): Terms for Change to an Issue Amount. A provision in an underwriting agreement, which allows members of the underwriting syndicate to purchase additional shares at the original price.
- **explanatoryNote** (en): Also known as a green shoe. Note that this set of terms does not refer to over-allotment as change to a the total issue amount issued to an individual investor. That would require separate but similar terms. FIBIM has "Over Allotment Amount" as an individual term.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
