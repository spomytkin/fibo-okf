---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preliminary prospectus
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The draft prospectus for the issue, as determined prior to marketing the issue. Certain terms in the draft prospectus
      will be finalized later in the issuance process to become the actual Prospectus. Term origin:DTCC issuance Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus
sources:
- id: fibo-source-4c4b98a252
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceDocuments.rdf
  sha256: 4c4b98a25292417c0cfa751a871d67e42ea9e85f29ea26acb47bf9860bbda08e
  title: FIBO source BP/SecuritiesIssuance/IssuanceDocuments.rdf
title: preliminary prospectus
type: Ontology Class
---

# preliminary prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus>

## Definition

The draft prospectus for the issue, as determined prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:DTCC issuance Reviews

## Relationships

- **Subclass of**: [Prospectus](/concepts/fibo/SEC/Securities/SecuritiesIssuance/Prospectus.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [OfferingDocumentTerms](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)

## Annotations

- **label** (en): preliminary prospectus
- **definition** (en): The draft prospectus for the issue, as determined prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:DTCC issuance Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
