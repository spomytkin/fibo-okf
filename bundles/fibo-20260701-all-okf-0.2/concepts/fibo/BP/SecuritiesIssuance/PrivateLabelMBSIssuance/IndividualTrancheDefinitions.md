---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: individual tranche definitions
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: In reality there is one termsheet that has sets of information for the terms for each Tranche. This class of information
      identifies the terms of one tranche, but it does not exist as a separate document in its own right. Further Notes ?
      We may need to firm up the relationship between the individual tranche termsheet and the information about the relationships
      among these (some of which are quite complex) and the terms that are common to more than one tranche. In practice these
      may be separate sections of one document. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondAmortizationPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CouponPaymentTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart
  - concept: /concepts/fibo/FND/Agreements/Contracts/TermSheet.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TermSheet
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IndividualTrancheDefinitions
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: individual tranche definitions
type: Ontology Class
---

# individual tranche definitions

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IndividualTrancheDefinitions>

## Definition

In reality there is one termsheet that has sets of information for the terms for each Tranche. This class of information identifies the terms of one tranche, but it does not exist as a separate document in its own right. Further Notes ? We may need to firm up the relationship between the individual tranche termsheet and the information about the relationships among these (some of which are quite complex) and the terms that are common to more than one tranche. In practice these may be separate sections of one document. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [TranchedMBSIssueProspectusPart](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md)
- **Subclass of**: [TermSheet](/concepts/fibo/FND/Agreements/Contracts/TermSheet.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [BondAmortizationPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [CouponPaymentTerms](/concepts/fibo/SEC/Debt/Bonds/CouponPaymentTerms.md)

## Annotations

- **label** (en): individual tranche definitions
- **definition** (en): In reality there is one termsheet that has sets of information for the terms for each Tranche. This class of information identifies the terms of one tranche, but it does not exist as a separate document in its own right. Further Notes ? We may need to firm up the relationship between the individual tranche termsheet and the information about the relationships among these (some of which are quite complex) and the terms that are common to more than one tranche. In practice these may be separate sections of one document. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
