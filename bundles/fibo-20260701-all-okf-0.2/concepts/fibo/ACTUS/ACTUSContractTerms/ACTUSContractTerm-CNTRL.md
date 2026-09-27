---
owl:
  annotations:
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterMapping
    value: Starting from the contract, this concept maps to (1) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty;
      cmns-rlcmp:isPlayedBy cmns-org:LegalPerson; cmns-id:isIdentifiedBy cmns-id:Identifier; cmns-txt:hasTextValue xsd:string
      or (2) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty; cmns-pts:actsOn (fibo-fnd-oac-own:Asset union
      fibo-fbc-dae-dbt:Collateral) or (3) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty; fibo-fnd-oac-own:isOwningParty
      fibo-fbc-pas-fpas:Position. Note that liability is not defined in FIBO which is a gap and should be added in parallel
      with asset.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is called the contract role in the ACTUS applicability rules.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This should really map to a union of roles that themselves map to the controlled vocabulary from the ACTUS specification
      for such roles (valid values). The roles may include buyer, seller, obligor, obligee, etc., or to a union of roles played
      by a financial asset or liability on the balance sheet of the legal entity playing the role. The challenge here is one
      of context, which requires rules to tease out completely.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CNTRL
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
title: ACTUSContractTerm-CNTRL
type: Ontology Individual
---

# ACTUSContractTerm-CNTRL

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CNTRL>

## Annotations

- **hasParameterMapping**: Starting from the contract, this concept maps to (1) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty; cmns-rlcmp:isPlayedBy cmns-org:LegalPerson; cmns-id:isIdentifiedBy cmns-id:Identifier; cmns-txt:hasTextValue xsd:string or (2) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty; cmns-pts:actsOn (fibo-fnd-oac-own:Asset union fibo-fbc-dae-dbt:Collateral) or (3) fibo-fnd-agr-ctr:hasContractParty fibo-fnd-agr-ctr:ContractParty; fibo-fnd-oac-own:isOwningParty fibo-fbc-pas-fpas:Position. Note that liability is not defined in FIBO which is a gap and should be added in parallel with asset.
- **explanatoryNote**: This is called the contract role in the ACTUS applicability rules.
- **explanatoryNote**: This should really map to a union of roles that themselves map to the controlled vocabulary from the ACTUS specification for such roles (valid values). The roles may include buyer, seller, obligor, obligee, etc., or to a union of roles played by a financial asset or liability on the balance sheet of the legal entity playing the role. The challenge here is one of context, which requires rules to tease out completely.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
