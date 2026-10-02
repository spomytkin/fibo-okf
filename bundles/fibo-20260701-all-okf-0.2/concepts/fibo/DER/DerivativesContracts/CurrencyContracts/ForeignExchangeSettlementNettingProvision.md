---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: foreign exchange settlement netting provision
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: settlement netting provision that is specific to foreign exchange contracts
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Foreign exchange settlement netting, if between two counterparties, which is also referred to as bilateral settlement
      netting in this case, can take one of two forms, payment netting or novation netting. Often, one of these two methods
      will be found in combination with close-out netting in master agreements between trading counterparties. Close-out netting,
      as distinct from payment or novation netting, provides for contract liquidation procedures in the event that one of
      the parties defaults under a contract or become bankrupt. Payment and novation netting describe the day-to-day processes
      of calculating and paying net amounts.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: FX settlement netting provision
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.newyorkfed.org/medialibrary/microsites/fxc/files/guidefx.pdf
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/SettlementNettingProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/SettlementNettingProvision
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeSettlementNettingProvision
sources:
- id: fibo-source-55979b6e85
  resource: references/fibo/DER/DerivativesContracts/CurrencyContracts.rdf
  sha256: 55979b6e85df3bd160e3c7ee545150e0b7c51792cecce55f507c06ba9978e0b6
  title: FIBO source DER/DerivativesContracts/CurrencyContracts.rdf
title: foreign exchange settlement netting provision
type: Ontology Class
---

# foreign exchange settlement netting provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/ForeignExchangeSettlementNettingProvision>

## Definition

settlement netting provision that is specific to foreign exchange contracts

## Relationships

- **See also**: [guidefx.pdf](<https://www.newyorkfed.org/medialibrary/microsites/fxc/files/guidefx.pdf>)
- **Subclass of**: [SettlementNettingProvision](/concepts/fibo/FND/Agreements/Contracts/SettlementNettingProvision.md)

## Annotations

- **label** (en): foreign exchange settlement netting provision
- **definition** (en): settlement netting provision that is specific to foreign exchange contracts
- **explanatoryNote** (en): Foreign exchange settlement netting, if between two counterparties, which is also referred to as bilateral settlement netting in this case, can take one of two forms, payment netting or novation netting. Often, one of these two methods will be found in combination with close-out netting in master agreements between trading counterparties. Close-out netting, as distinct from payment or novation netting, provides for contract liquidation procedures in the event that one of the parties defaults under a contract or become bankrupt. Payment and novation netting describe the day-to-day processes of calculating and paying net amounts.
- **synonym**: FX settlement netting provision

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
