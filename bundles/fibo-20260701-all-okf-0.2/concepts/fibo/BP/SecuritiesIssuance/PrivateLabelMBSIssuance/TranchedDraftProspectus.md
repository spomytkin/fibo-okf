---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranched draft prospectus
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The draft prospectus for a tranched Mortgage Backed Securities issue, as determined by the issuing entity prior
      to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become
      the actual Prospectus. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedDraftProspectus
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: tranched draft prospectus
type: Ontology Class
---

# tranched draft prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedDraftProspectus>

## Definition

The draft prospectus for a tranched Mortgage Backed Securities issue, as determined by the issuing entity prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [PreliminaryProspectus](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md)

## Constraints

- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [TranchedMBSDealProspectus](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md)

## Annotations

- **label** (en): tranched draft prospectus
- **definition** (en): The draft prospectus for a tranched Mortgage Backed Securities issue, as determined by the issuing entity prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
